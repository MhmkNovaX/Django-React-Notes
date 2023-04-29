import React from "react";
import {useForm} from 'react-hook-form'

const UserForm = () => {
    const {register, handleSubmit} = useForm()
    const onSubmit = data => console.log(data)
    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="mb-3">
                <label htmlFor="username" className="form-label"
                       {...register("username", {required: "Enter Username"})}>Username:</label>
                <input type="text" className="form-control" id="username"/>
            </div>
            <div className="mb-3">
                <label htmlFor="password" className="form-label"
                       {...register("password", {required: "Enter Password"})}>Password:</label>
                <input type="password" className="form-control" id="password"/>
            </div>
            <input type="submit" className="btn btn-primary" value="Submit!"/>
        </form>
    )
}

export default UserForm