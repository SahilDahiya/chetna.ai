from textwrap import dedent

PASSAGE_TO_SVG_PROMPT = dedent("""\   
   <svg_visualization_prompt>
      
      <description>
         Convert philosophical text passage into an SVG visualization with specific styling and highlighting requirements.
      </description>
      
      <requirements>
         <svg_specs>
            <background color="#1a1a1a"/>
            <base_text color="#e0e0e0" font_family="Arial" size="16px"/>
            <book_title size="20px" weight="bold"/>
            <chapter_reference color="#808080" size="14px"/>
         </svg_specs>
         
         <highlight_colors>
            <color name="main_concepts" hex="#4a9eff" description="blue"/>
            <color name="core_arguments" hex="#ff7070" description="red"/>
            <color name="metaphors" hex="#70ff70" description="green"/>
            <color name="paradoxes" hex="#ffff70" description="yellow"/>
            <color name="lists_qualities" hex="#ff70ff" description="magenta"/>
            <color name="key_conclusions" hex="#70ffff" description="cyan"/>
            <color name="philosophical_statements" hex="#ff9670" description="orange"/>
         </highlight_colors>
         
         <layout_rules>
            <rule>Compact layout with proper text wrapping</rule>
            <rule>Maintained paragraph structure</rule>
            <rule>No extra space at bottom</rule>
         </layout_rules>
      </requirements>

      <input_structure>
         <book name="{book_name}"/>
         <chapter name="{chapter_name}"/>
         <passage number="{passage_no}">
            {passage}
         </passage>
      </input_structure>

      <example>
         <passage_text>
            Unconditional Duties.—All men who feel that they need the strongest
            words and intonations, the most eloquent gestures and attitudes, in
            order to operate at all—revolutionary politicians, socialists,
            preachers of repentance with or without Christianity, with all of whom
            there must be no mere half-success,—all these speak of "duties," and
            indeed, always of duties, which have the character of being
            unconditional—without such they would have no right to their excessive
            pathos: they know that right well! [...]
         </passage_text>
         
         <svg_code>
            <![CDATA[
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
                  <!-- Background -->
                  <rect width="800" height="600" fill="#1a1a1a"/>
                  
                  <!-- Title -->
                  <text x="40" y="40" fill="#e0e0e0" font-family="Arial, sans-serif" font-size="20" font-weight="bold">
                     Joyous Wisdom
                  </text>
                  
                  <!-- Chapter and Passage -->
                  <text x="40" y="70" fill="#808080" font-family="Arial, sans-serif" font-size="14">
                     Chapter 1, Passage 5
                  </text>
                  
                  <!-- Text container -->
                  <foreignObject x="40" y="90" width="720" height="480">
                     <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: Arial, sans-serif; color: #e0e0e0; font-size: 16px; line-height: 1.6;">
                        <!-- Example text content with highlighting -->
                     </div>
                  </foreignObject>
            </svg>
            ]]>
         </svg_code>
      </example>

      <output_requirements>
         <requirement>Provide complete SVG code implementing all specified requirements</requirement>
         <requirement>Include all necessary XML namespaces and attributes</requirement>
         <requirement>Ensure proper text wrapping and layout within the SVG</requirement>
      </output_requirements>
   </svg_visualization_prompt>
    """\
    )  # noqa: E501
