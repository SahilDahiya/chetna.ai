from joyous_wisdom.joyous_wisdom_repository import JoyousWisdomPassage, JoyousWisdomRepository
from pymongo import MongoClient

mongo_client = MongoClient(
    'mongodb://localhost:27017/',
    uuidRepresentation='standard',
    tz_aware=True,
)

repository = JoyousWisdomRepository(mongo_client, 'nietzsche')


def extract_passages(text):
    """
    Extract passages from text and return a list of dictionaries containing:
    - chapter_name: Name of the chapter (including BOOK FIRST, JEST, RUSE AND REVENGE, etc.)
    - passage_no: Passage number
    - text: Full text of the passage

    Args:
        text (str): Input text to process

    Returns:
        list: List of dictionaries containing passage information
    """
    passages = []
    current_chapter = None
    lines = text.split('\n')

    passage_text = []
    current_passage_no = None

    for i, line in enumerate(lines):
        # Detect chapter names - now includes both patterns
        stripped_line = line.strip()
        if stripped_line.startswith('BOOK '):
            current_chapter = stripped_line
            continue
        elif stripped_line == 'JEST, RUSE AND REVENGE.':
            # Check next line for subtitle
            if i + 1 < len(lines) and 'PRELUDE IN RHYME' in lines[i + 1]:
                current_chapter = stripped_line + ' ' + lines[i + 1].strip()
            else:
                current_chapter = stripped_line
            continue

        # Detect passage numbers (format: number followed by period)
        if stripped_line and stripped_line[0].isdigit() and '.' in stripped_line:
            # If we were building a previous passage, save it
            if passage_text and current_passage_no is not None:
                passages.append(
                    {
                        'chapter_name': current_chapter,
                        'passage_no': current_passage_no,
                        'text': '\n'.join(passage_text).strip(),
                    }
                )

            # Start new passage
            parts = stripped_line.split('.', 1)
            # Remove the try-except block since we're no longer converting to int
            current_passage_no = parts[0]  # Keep as string
            passage_text = [parts[1].strip()] if len(parts) > 1 else []

        # Add lines to current passage
        elif current_passage_no is not None and stripped_line:
            passage_text.append(stripped_line)

    # Don't forget to add the last passage
    if passage_text and current_passage_no is not None:
        passages.append(
            {'chapter_name': current_chapter, 'passage_no': current_passage_no, 'text': '\n'.join(passage_text).strip()}
        )

    for passage in passages:
        try:
            repository.save(JoyousWisdomPassage(**passage))
        except Exception as e:
            print(f'passage_not_added({e})')


# Example usage:
if __name__ == '__main__':
    with open('passageDB\joyous_wisdom\joyous_wisdom.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    extract_passages(text)
