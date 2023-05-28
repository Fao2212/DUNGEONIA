import React, { useEffect, useState } from "react";
import { Button, Container, Form, Row, Navbar, Nav, Spinner } from "react-bootstrap"
import { useNavigate } from "react-router-dom";

function ShowDescriptionBox(props) {
    const [characterDescription, setCharacterDescription] = useState("")
    const [isLoading, setLoading] = useState(false)
    let navigate = useNavigate();
    const goHome = () => {
        let path = `home`;
        navigate(path);
    }

    async function ButtonFunctionallity() {
        const request = { "characterDescription": characterDescription }
        setLoading(true)
        const respose = await fetch("/createCharacter", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(request)
        }).then(respose => respose.json()).then(
            data => {
                goHome()
            }
        )
    }

    if (props.userExist === false) {
        if (isLoading === false) {
            return <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>Character Descrtiption</Form.Label>
                <Form.Control as="textarea" rows={3} placeholder="Enter a description for your character" onChange={e => setCharacterDescription(e.target.value)} />
                <Button onClick={ButtonFunctionallity}>
                    Create
                </Button>
            </Form.Group>
        }
        else {
            return <Spinner animation="grow" variant="warning" />
        }
    }
    else {
        return null
    }
}


export const Login = () => {

    const [userName, setUserName] = useState("")
    const [userExist, setUserExist] = useState(true)

    let navigate = useNavigate();
    const goHome = () => {
        let path = `home`
        navigate(path)
    }

    async function ButtonFunctionallity() {
        const request = { "userName": userName }
        const respose = await fetch("/tryLogin", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(request)
        }).then(respose => respose.json()).then(
            data => {
                setUserExist(data.exist)
                if (data.exist) {
                    goHome()
                }
            }
        )
    }

    function LoginButton() {
        if (userExist) {
            return <Button onClick={ButtonFunctionallity}>Login</Button>
        }
        else {
            return null
        }
    }

    return <Container>
        <Row className="px-4 my-5">
            <Form>
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Character name</Form.Label>
                    <Form.Control type="text" placeholder="Enter a name for your character" onChange={e => setUserName(e.target.value)} />
                </Form.Group>
                <ShowDescriptionBox userExist={userExist} />
            </Form>
        </Row>
        <Row className="px-4 my-5">
            <LoginButton />
        </Row>
    </Container>

}