# Custom Tailwind Configurations

## Basic Customization
**Customizing Colors**
Tailwind comes with a default palette, but you can define your own colors by editing the `tailwind.config.js` file like so:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'branding-blue': '#5ca9fb',
        'branding-red': '#f56565',
      }
    }
  }
}
```

**Font Families**
To add custom fonts, first import them, then update the `tailwind.config.js`:
```javascript
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', 'sans-serif'],
        serif: ['Merriweather', 'serif'],
      }
    }
  }
}
```

**Breakpoints**

```javascript
module.exports = {
  theme: {
    extend: {
      screens: {
        '2xl': '1440px',
        '3xl': '1920px',
      }
    }
  }
}
```

**Custom Utilities**
The `addUtilities` function takes two parameters:

- The first parameter is an object where the keys are the class names and the values are the CSS styles.

- The second parameter is an array of variants you want to generate for these utilities, such as responsive, hover, focus, etc.

```javascript
module.exports = {
  plugins: [
    function({ addUtilities }) {
      const newUtilities = {
        '.filter-none': {
          filter: 'none',
        },
        '.filter-grayscale': {
          filter: 'grayscale(100%)',
        },
      }

      addUtilities(newUtilities, ['responsive', 'hover']);
    }
  ],
}
```