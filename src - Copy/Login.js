import React, { useEffect, useState } from "react";
import { Button, Container, Form, Row, Navbar, Nav } from "react-bootstrap"

function Home() {
    return (
        <div className='App'>
            <header>
                <Navbar bg="dark" variant="dark" expand="lg">
                    <Container>
                        <Navbar.Brand href="#home">DungeonIA</Navbar.Brand>
                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                        <Navbar.Collapse id="basic-navbar-nav">
                            <Nav className="me-auto">
                                <Nav.Link href="/home">Home</Nav.Link>
                                <Nav.Link href="/character">Character</Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
            </header>
            <main>
                <Container>
                    <Row className="px-4 my-5">
                        <Form>
                            <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                                <Form.Label>Player Input</Form.Label>
                                <Form.Control type="text" placeholder="Write a description for your adventure..." />
                            </Form.Group>
                            <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                                <Form.Label>Adventure</Form.Label>
                                <Form.Control as="textarea" rows={3} readOnly />
                            </Form.Group>
                        </Form>
                        <Button>
                            Send Descrtiption
                        </Button>
                    </Row>

                </Container>
            </main>
        </div>
    )
}

function Character() {
    const [character, setCharacter] = useState("")
    return <div>Character</div>
}

function ShowDescriptionBox(props) {
    const [characterDescription, setCharacterDescription] = useState("")

    async function ButtonFunctionallity() {
        const request = { "characterDescription": characterDescription }
        const respose = await fetch("/createCharacter", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(request)
        }).then(respose => respose.json()).then(
            data => {
                //setUserExist(data.exist)  
            }
        )
    }

    if (props.userExist === false) {
        return <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
            <Form.Label>Character Descrtiption</Form.Label>
            <Form.Control key={"game1"} as="textarea" rows={3} placeholder="Enter a description for your character" onChange={e => setCharacterDescription(e.target.value)} />
            <Button onClick={ButtonFunctionallity}>
                Create
            </Button>
        </Form.Group>
    }
    else {
        return null
    }
}


export const Login = () => {

    const [userName, setUserName] = useState("")
    const [userExist, setUserExist] = useState(true)

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