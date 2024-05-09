# Coding for Screenreaders

### Screen Reader Announcements
Changes in the state of UI components (like opening or closing of submenus) hould be announced properly:

`aria-live` Regions: Introduce sections of the page that are marked with `aria-live="polite"` or `aria-live="assertive"` for dynamic content changes, so that screen readers can announce these changes when they occur without disrupting the user's current activity.

### Labeling and Instructions

Descriptive Labels: 
All elements, especially interactive ones like buttons, should have clear and descriptive labels using `aria-label`.

Instructions for  Navigation: Provide instructions at the beginning of the navigation section on how to interact with the menu, especially for complex interfaces.

### Text Alternatives for Visual Information
Visual Cues as Text: If visual cues like colors or styles are used to indicate active or disabled states, these should be conveyed through text or screen reader-specific hints.


### Logical Tab Order
Consistent Navigation: Users should be able to navigate through items in a predictable and consistent order, matching the visual structure of the component.

### Skip Navigation Link

Skip to Main Content: Provide a "Skip to main content" link at the top of the page that becomes visible when focused (done via keyboard navigation).
