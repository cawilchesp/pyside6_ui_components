# :root {
#   Styleguide Nord - Polar Night
  
#   --nord0: #2e3440;
#   --nord1: #3b4252;
#   --nord2: #434c5e;
#   --nord3: #4c566a;

#   Styleguide Nord - Snow Storm
  
#   --nord4: #d8dee9;
#   --nord5: #e5e9f0;
#   --nord6: #eceff4;

#   Styleguide Nord - Frost
  
#   --nord7: #8fbcbb;
#   --nord8: #88c0d0;
#   --nord9: #81a1c1;
#   --nord10: #5e81ac;
  
#   Styleguide Nord - Aurora
  
#   --nord11: #bf616a;
#   --nord12: #d08770;
#   --nord13: #ebcb8b;
#   --nord14: #a3be8c;
#   --nord15: #b48ead;
# }


def colors(theme: bool, role: str) -> str:
    light = {
        'background': '#eceff4',
        'on_background': '#001f2a',
        'surface_tint': '#d8dee9',
        'surface': '#eceff4',
        'on_surface': '#001f2a',
        'surface_variant': '#dfe2eb',
        'on_surface_variant': '#43474e',
        'outline': '#73777f',

        'primary': '#5e81ac',
        'on_primary': '#2e3440',
        'secondary': '#81a1c1',
        'on_secondary': '#2e3440',
        'tertiary': '#8fbcbb',
        'on_tertiary': '#2e3440',

        'hover': '#88c0d0',




        'error': '#ba1a1a',
        'error_container': '#ffdad6',
        'on_error': '#ffffff',
        'on_error_container': '#410002',
        
        'inverse_on_surface': '#e1f4ff',
        'inverse_surface': '#003547',
        'inverse_primary': '#a2c9ff',
        'shadow': '#000000',
        'outline_variant': '#c3c6cf',
        'scrim': '#000000'
    }

    dark = {
        'background': '#2e3440',
        'on_background': '#bfe9ff',
        'surface_tint': '#4c566a',
        'surface': '#2e3440',
        'on_surface': '#bfe9ff',
        'surface_variant': '#43474e',
        'on_surface_variant': '#c3c6cf',
        'outline': '#8d9199',

        'primary': '#81a1c1',
        'on_primary': '#eceff4',
        'secondary': '#5e81ac',
        'on_secondary': '#eceff4',
        'tertiary': '#8fbcbb',
        'on_tertiary': '#eceff4',

        'hover': '#88c0d0',



        'error': '#ffb4ab',
        'error_container': '#93000a',
        'on_error': '#690005',
        'on_error_container': '#ffdad6',

        'inverse_on_surface': '#001f2a',
        'inverse_surface': '#bfe9ff',
        'inverse_primary': '#0060a8',
        'shadow': '#000000',
        'outline_variant': '#43474e',
        'scrim': '#000000'
    }

    if theme:
        return light[role]
    else:
        return dark[role]