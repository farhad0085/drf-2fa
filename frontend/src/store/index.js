import { createStore, compose, applyMiddleware } from "redux";
import rootReducer from "./reducers/rootReducer";
import thunk from "redux-thunk";

let composers = [applyMiddleware(thunk)];

if (process.env.REACT_APP_ENVIRONMENT === "development") {
  if (window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) {
    composers.push(window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__());
  }
}

const store = createStore(rootReducer, compose(...composers));

export default store;
