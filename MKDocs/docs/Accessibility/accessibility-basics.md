# Writing Accessible Code

Make your HTML code as semantic as possible.

### Use Semantic HTML
Purpose: Semantic HTML elements clearly describe their meaning in a human- and machine-readable way.

Examples: Use `<header>`, `<footer>`, `<article>`, `<section>`, `<nav>`, and `<aside>` to structure the content. Use `<h1>`to `<h6>` for headings to structure content logically.

### Alt Text for Images
Purpose: Provides a textual alternative to non-text content in web pages.

Example: `<img src="logo.png" alt="Company Logo">` — The alt attribute explains the image content.

### ARIA (Accessible Rich Internet Applications) Roles
Purpose: ARIA roles and attributes provide additional information about the role, state, and functionality of elements.

Example: `aria-label`, `aria-hidden`, `aria-live` are commonly used.

### Keyboard Accessibility
Purpose: All functionalities should be accessible via a keyboard.

Example: All interactive elements like links, buttons, and form controls are focusable using the tabindex attribute if necessary.

### Accessible Forms
Purpose: Ensure forms are usable and understandable.

Example:
Use `<label>` for every input element. For example, `<label for="name">Name:</label><input type="text" id="name">`.
Group related form elements within `<fieldset>` elements and describe the group with `<legend>`.

### Use of Correct Headings and Labels
Purpose: Headings and labels help in structuring content and describing functionality.

Example: Use headings consistently to structure content; labels should clearly describe the purpose of the associated input field.

### Manage Focus for Interactive Elements
Purpose: Focus management is crucial for users who rely on keyboards and assistive technologies. Can programatically set through `element.focus()`.

Example: When a modal opens, move focus to the modal, and trap focus within until it’s closed.

### Sufficient Color Contrast
Purpose: Text should be readable against its background for those with visual impairments. Note that some color combinations techincally pass color contrast checkers but are deemed harder to read in actuality.

Example: Use tools like the WebAIM Color Contrast Checker to ensure that text-background color combinations have enough contrast.

### Responsive and Mobile Accessibility
Purpose: Content must be usable on all devices and screen sizes.

Example: Use responsive web design practices, such as flexible grid layouts and media queries.