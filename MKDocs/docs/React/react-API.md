# Basic React APIs

## Introduction

React APIs are a way for a React application to interact with external services. They allow the application to send and receive data, enabling it to be dynamic and responsive.

## Types of APIs

### ReactDOM

This API provides methods for rendering React components into the DOM (Document Object Model). The `ReactDOM.render()` method is commonly used to mount a React component into a specific DOM node.

### Components

Components are the building blocks of React applications. They can be either functional components or class components. Functional components are simple JavaScript functions that return JSX (JavaScript XML), while class components are JavaScript classes that extend `React.Component` and implement a `render()` method.

### Props

Props (short for properties) are inputs to React components. They allow data to be passed from parent components to child components. Props are read-only and should not be modified by the component itself.

### State

State represents the internal data of a component. Unlike props, which are passed down from parent components, state is managed within the component itself. Changes to state trigger re-rendering of the component, updating the UI as necessary. State can be initialized in the constructor of a class component or using the `useState` hook in functional components.

### Hooks

Hooks are functions that enable functional components to use state and other React features without writing a class. Commonly used hooks include `useState`, `useEffect`, `useContext`, and `useReducer`.