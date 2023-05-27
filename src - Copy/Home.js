import React, {useState,useEffect} from 'react'
import {Button,Navbar,Container,Form,Nav, Row} from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"
export const Home = () =>
{
    const [data,setData] = useState([{}])

    useEffect(()=>{
      fetch("/home").then(
        res => res.json()
      ).then(
        data =>{
          setData(data)
          console.log(data)
        }
      )
    },[])
  
    return (
      <div className='App'>
        <header>
          <Navbar bg="dark" variant="dark" expand="lg">
          <Container>
            <Navbar.Brand href="#home">DungeonIA</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#character">Character</Nav.Link>
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