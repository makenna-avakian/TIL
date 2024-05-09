# Setting Up Tailwind CSS with Vite

Vite is a modern frontend building tool which makes dev much easier. Using tailwind with Vite requires a few extra steps.


## Create New Project

```javascript 
npm create vite@latest my-vite-app -- --template vanilla
```

Set up your Vite project like so:

```
cd my-vite-app
```

## Install Tailwind

```
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

Init Tailwind Files:

```
npx tailwindcss init -p
```
This command creates a `tailwind.config.js` and a `postcss.config.js` file in your project directory.

## Configure Tailwind

Edit the tailwind.config.js file to enable purge in production. This step helps to remove unused CSS to optimize the final build size. Update the content path to match the files where you use Tailwind classes:

```
module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx,vue}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

*Vite projects specifically need index.html added.

## Include Tailwind in your CSS and import in main

You may need to create a file if you don't already have one.

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
Import this into your main file.

```
import './style.css';
```