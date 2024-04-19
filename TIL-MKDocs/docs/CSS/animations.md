# CSS Animations

CSS animations add visual effects to HTML elements on a web page. They are widely used to create interactive and dynamic effects without using JavaScript/Typescript. 

## CSS @keyframes Rule

The foundation of css animations is the `@keyframes` rule, which specifies the animation's behavior. With `@keyframes`, you can define the state of the animation at various points using percentages. For example, 0% represents the start of the animation, and 100% represents the end, while 50% is the middle.

```javascript
@keyframes example {
    0% { background-color: red; }
    50% { background-color: yellow; }
    100% { background-color: green; }
}
```

## Common Animation Properties

`animation-name`: Specifies the name of the @keyframes animation.

`animation-duration`: Defines how long the animation should take to complete.

`animation-timing-function`: Controls the animation's speed curve (e.g., linear, ease-in, ease-out, ease-in-out).

`animation-delay`: Sets a delay before the animation starts.

`animation-iteration-count`: Determines how many times the animation should repeat.

`animation-direction`: Defines whether the animation should run forwards, backwards, or alternate between the two.

`animation-fill-mode`: Specifies a style when the animation is not playing (before it starts, after it ends, or both).

`animation-play-state`: Allows pausing and resuming the animation.


## Typical Applications

**Button Hover Effects**
create subtle hover effects for buttons. An example is changing the background color when the user hovers over it.

**Loading Spinners** implement custom loading animations such as spinners or progress bars. These are used to make loading times feel more interactive and encourage the user to feel like things are happening.

**Attention Seekers** draw attention to specific elements like notifications or buttons, using different effects.

## Benefits of CSS Animations

**Performance**: CSS animations are very performant.

**Control**: CSS animations give you exact control over animation timing and behavior.

**Compatibility**: CSS Animations are supported widely across modern web browsers without additional libraries.

## Limitations of CSS Animations
**Complexity**: More complex animations can become difficult to manage with pure CSS.

**Control**: The download to control is that unlike JavaScript, real-time manipulation based on user input or other dynamic conditions is limited. However, it can be used with Javascript to great effect.