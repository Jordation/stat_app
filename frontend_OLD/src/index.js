import React from 'react';
import ReactDOM from 'react-dom/client';
import {
    createBrowserRouter,
    RouterProvider,

} from "react-router-dom";
import UrlToGraphs from "./pages/custom-graphs/UrlToGraphs";
import BasePage from "./pages/base/base";

const router = createBrowserRouter([
    {
        path: "/",
        element: < BasePage />
    },
    {
        path: "/custom",
        element: < UrlToGraphs />
    }
]);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <RouterProvider router={ router } />
  </React.StrictMode>
);

