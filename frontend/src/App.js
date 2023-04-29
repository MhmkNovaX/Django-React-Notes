import React from "react";
import Navbar from "./components/Navbar/Navbar";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import SignIn from "./pages/SignIn";

const App = () => {
  return (
      <BrowserRouter>
          <Navbar />
          <main>
              <Routes>
                  <Route exact path={"login"} element={<SignIn />} />
              </Routes>
          </main>

      </BrowserRouter>
  )
}

export default App