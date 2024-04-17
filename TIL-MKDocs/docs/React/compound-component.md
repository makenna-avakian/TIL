# Compound Components

A compound component is a react pattern which allows you to share a commmon state within a component structure while maintaining a relationship between a parent component and it's children.

## How Compound Components Work

**Structure**: A compound component consists of a parent component and one or more child components. The parent component typically manages the shared state or functionality.

**State Sharing**: The parent component can pass down state, functions, or any other necessary props to its children without having to pass props explicitly at every level.

**Flexibility**: You can adjust the children in different ways to achieve flexible layouts while still maintaining a controlled behavior managed by the parent.

