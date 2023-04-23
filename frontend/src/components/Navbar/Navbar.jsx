import React from "react";

import './style.module.css'
import Logo from "./Logo/Logo";

const Navbar = () => {
    return (
        <nav className={"px-5 py-3 row"}>
            <Logo className={"col-8"} />

        </nav>
    )
}

export default Navbar