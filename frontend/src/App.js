import React from "react"
import {Route, createBrowserRouter, createRoutesFromElements, RouterProvider,Link, BrowserRouter, Outlet} from "react-router-dom"
import {Login} from "./Login"
import {Character} from "./Character"
import {Home} from "./Home"


function App() {

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route exact path = "/" element={<Root />}>
        <Route index element={<Login/>}/>
        <Route exact path = "/home" element={<Home />}/>
        <Route exact path = "/character" element={<Character />}/>
      </Route>
    )
  )

  return(
    <div className="App">
      <RouterProvider router={router}/>
    </div>
  )
}

const Root = () =>{
  return(
    <>
    <div>
    </div>
    <div>
      <Outlet/>
    </div>
    </>
  )
}

export default App