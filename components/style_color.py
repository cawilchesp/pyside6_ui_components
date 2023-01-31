def colors(theme: bool, role: str) -> str:
    light = {
        'primary': '#0060a8',
        'on_primary': '#ffffff',
        'hover_primary': '#200060a8',
        'primary_container': '#d3e4ff',
        'on_primary_container': '#001c38',
        'hover_primary_container': '#20d3e4ff',

        'secondary': '#00629d',
        'on_secondary': '#ffffff',
        'hover_secondary': '#2000629d',
        'secondary_container': '#cfe5ff',
        'on_secondary_container': '#001d34',
        'hover_secondary_container': '#20cfe5ff',

        'tertiary': '#004ee8',
        'on_tertiary': '#ffffff',
        'tertiary_container': '#dce1ff',
        'on_tertiary_container': '#001550',

        'error': '#ba1a1a',
        'error_container': '#ffdad6',
        'on_error': '#ffffff',
        'on_error_container': '#410002',
        'background': '#fafcff',
        'on_background': '#001f2a',
        'surface': '#fafcff',
        'on_surface': '#001f2a',
        'surface_variant': '#dfe2eb',
        'on_surface_variant': '#43474e',
        'outline': '#73777f',
        'inverse_on_surface': '#e1f4ff',
        'inverse_surface': '#003547',
        'inverse_primary': '#a2c9ff',
        'shadow': '#000000',
        'surface_tint': '#a2c9ff',
        'outline_variant': '#c3c6cf',
        'scrim': '#000000'
    }

    dark = {
        'primary': '#a2c9ff',
        'on_primary': '#00315b',
        'hover_primary': '#20a2c9ff',
        'primary_container': '#004881',
        'on_primary_container': '#d3e4ff',
        'hover_primary_container': '#20004881',

        'secondary': '#99cbff',
        'on_secondary': '#003355',
        'hover_secondary': '#2099cbff',
        'secondary_container': '#004a78',
        'on_secondary_container': '#cfe5ff',
        'hover_secondary_container': '#20004a78',

        'tertiary': '#b6c4ff',
        'on_tertiary': '#002780',
        'tertiary_container': '#003ab3',
        'on_tertiary_container': '#dce1ff',

        'error': '#ffb4ab',
        'error_container': '#93000a',
        'on_error': '#690005',
        'on_error_container': '#ffdad6',
        'background': '#001f2a',
        'on_background': '#bfe9ff',
        'surface': '#001f2a',
        'on_surface': '#bfe9ff',
        'surface_variant': '#43474e',
        'on_surface_variant': '#c3c6cf',
        'outline': '#8d9199',
        'inverse_on_surface': '#001f2a',
        'inverse_surface': '#bfe9ff',
        'inverse_primary': '#0060a8',
        'shadow': '#000000',
        'surface_tint': '#0060a8',
        'outline_variant': '#43474e',
        'scrim': '#000000'
    }

    if theme:
        return light[role]
    else:
        return dark[role]