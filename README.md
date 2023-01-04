# React Interview Questions

## Overview

In this repository are several React interview questions designed to test a candidates knowledge on specific areas.

Each question is designed to deal with a specific area of knowledge, and includes a task based on sample code as well as follow up questions/directionals which can be used to gauge more about the candidates experience/choices in that area.

## State and Data Management

### Context

The desire here is to assess the candidates ability to recognize different ways of managing data within React, and provide arguments for choice depending on application context.

### Sample Code

```js
import React from 'react'
import { connect } from 'react-redux';

const Container = ({ userDetails }) => {
    return (
        <h1>Page Heading</h1>
        <UserDetails address={userDetails.address} name={userDetails.name} />
    );
}

const UserDetails = ({ address, name}) => {

    return (
        <div>
            <h2>{name}</h2>
            <UserAddress address={address} />
        </div>
    );
}

const UserAddress = ({ line1, line2, postcode, country}) => {
    return (
        <div>
            <p>{line1}</p>
            <p>{line2}</p>
            <UserAddressPostcode value={postcode}/>
        </div>
    );
}

const UserAddressPostcode = ({ value }) => {
    return (<span>{value}</span>);
}

const mapStateToProps = (state) => {
    return {
        userDetails: state.userDetails,
    }
}

export default connect(mapStatetoProps)(Container);
```

### Task

Given the code sample, can you do the following:

**Refactor use of props through the components so that interim components aren't accessing data they don't need**

Ideal output:

- Uses React Context API in order to create a provider/consumer pair that holds/makes available the user's details

**Refactor the code so that it uses local state (`useState()` hook) rather than redux**

### Follow ups/Directionals

- What's the value of using external state management like redux? When would you not use it?
- What are the down-sides of prop drilling?
- How would you test your refactored code (typically)?

## Working with async and common hooks

### Context

The desire here is to asses the candidate's understanding of working with async code within components, and formatting data.

### Sample Code

```js
// Pretend this is an actual API call
const getData = () =>
  Promise.resolve({
    Monday: "Google",
    Tuesday: "Tesla",
    Wednesday: "Microsoft",
    Thursday: "Apple",
    Friday: "T. Rowe Price",
    Saturday: "Facebook",
    Sunday: "Twitter",
  });

const Container = () => {
  const refeshData = () => {
    return getData();
  };

  return (
    <ul>
      <li>#day - #company</li>
    </ul>
  );
};
```

### Task

Given the code sample, can you do the following:

**Complete the code using `getData()` so that the data is displayed in an `<ul>` as per the format when the component is rendered?**

Ideal output:

- Use of `useEffect()` hook for triggering the API call
- Formatting the parent data structure from object --> array (e.g. `Object.entries(...).map(...)`)
- Storage of data in state (`useState()`)
- Mapping over the stored array to print values as per example

Bonus points for remembering to add a `key` prop to each `<li>`

**Add the capability to refresh the data when the `<button>` element is clicked?**

Ideal output:

- Use of `useCallback()`
- Update the state as per previous question

### Follow ups/Directionals

- How would you typically handle API errors?
- How would you go about testing this?

## Working with portals and refs

### Context

The desire here is to assess the candidate's understanding of lesser used React APIs - that are more likely to come into play when dealing with embedded applications or DOM manipulation.

### Sample Code

index.html

```html
<body>
  <div id="app"></div>
  <div id="randomNode"></div>
</body>
```

app.js

```js
const PopupBox = () => {
  return <div>Hey, guess who's back?</div>;
};

const ImageSizer = ({ src }) => {
  const imageHeight = 0,
    imageWidth = 0;
  return (
    <>
      <img src={src} />
      <span className="caption">
        Image Width: {imageWidth} | Image Height: {imageHeight}
      </span>
    </>
  );
};

const App = () => {
  return (
    <>
      <h1>Page Title</h1>
      <PopupBox />
    </>
  );
};

ReactDOM.render(document.getElementById("app"), <App />);
```

### Task

Given the code sample, can you do the following:

**Refactor `<PopupBox>` to render it's returned child into `#popupBox`**

Ideal output:

- Uses `React.createPortal()` to render the returned value of `<PopupBox>`

**Complete <ImageSizer> so that it prints the correct image width and height using hooks**

Ideal output:

- Use `useRef()` in order to fetch the height and width from `<img/> `
