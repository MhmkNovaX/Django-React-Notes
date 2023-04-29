import React from "react";
import { useForm } from 'react-hook-form'
import UserForm from "../components/UserForm/UserForm";


const SignIn = () => {
    const { register, handleSubmit } = useForm()
    const onSubmit = data => console.log(data)

    return (
        <>
            <UserForm />
        </>
    )
}

export default SignIn