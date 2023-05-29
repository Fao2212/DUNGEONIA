import React, { useState, useEffect } from 'react'
import { Button, Navbar, Container, Form, Nav, Row, Col, Spinner } from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

function AdventureState(props) {
  const [loading, setLoading] = useState(false)
  const [playerInput, setPlayerInput] = useState("")
  const [canPlayAdventure, setCanPlayAdventure] = useState(true)
  const [adventureStarted, setAdventureStarted] = useState(false)

  async function StartButtonFunctionallity() {
    var theLines = props.playerLines
    theLines += `${playerInput}\n-`
    props.setPlayerLines(theLines)
    setPlayerInput("")
    setAdventureStarted(true)
    setLoading(true)
    //Hacer peticion
    const request = { "adventureDescription": playerInput }
    const respose = await fetch("/startAdventure", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(request)
    }).then(
      res => res.json().then(
        data => {
          props.setadventureLines(data.adventure)
          setLoading(false)
        }
      )
    )
  }

  async function NextButtonFunctionallity() {
    var theLines = props.playerLines
    theLines += `${playerInput}\n-`
    props.setPlayerLines(theLines)
    setPlayerInput("")
    setLoading(true)
    //Hacer peticion
    const request = { "userEventDescription": playerInput }
    const respose = await fetch("/nextTurn", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(request)
    }).then(
      res => res.json().then(
        data => {
          props.setadventureLines(data.adventure)
          setLoading(false)
          if(!data.canPlayAdventure){
            setCanPlayAdventure(false)
          }
        }
      )
    )
  }

  if (loading) {
    return <Spinner animation="grow" variant="warning" />
  }
  else {
    if (canPlayAdventure) {
      if (adventureStarted)
        return <div>
          <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
            <Form.Label>Player Input</Form.Label>
            <Form.Control type="text" placeholder="Write a description for your adventure..." value={playerInput} onChange={e => setPlayerInput(e.target.value)} />
          </Form.Group>

          <Button onClick={NextButtonFunctionallity}>
            Next Turn
          </Button>
        </div>
      else
        return <div>
          <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
            <Form.Label>Player Input</Form.Label>
            <Form.Control type="text" placeholder="Write a description for your adventure..." value={playerInput} onChange={e => setPlayerInput(e.target.value)} />
          </Form.Group>

          <Button onClick={StartButtonFunctionallity}>
            Start Adventure
          </Button>

        </div>
    }
    else {
      return null
    }
  }
}


export const Home = () => {
  const [playerLines, setPlayerLines] = useState("-")
  const [adventureLines, setadventureLines] = useState("-")

  return (
    <div className='App'>
      <header>
        <Navbar bg="dark" variant="dark" expand="lg">
          <Container>
            <Navbar.Brand href="/home">DungeonIA</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="/character">Character</Nav.Link>
                <Nav.Link href="/">Log Out</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </header>
      <main>
        <Container>
          <Row className="px-4 my-5">
            <AdventureState
              playerLines={playerLines}
              setPlayerLines={(e) => { setPlayerLines(e) }}
              adventureLines
              setadventureLines={(e) => { setadventureLines(e) }}
            />
          </Row>
          <Row className="px-4 my-5">
            <Col sm={8}>
              <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>Adventure</Form.Label>
              </Form.Group>
            </Col>
            <Col>
              <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Label>Player Inputs</Form.Label>

              </Form.Group>
            </Col>
            <Row className="px-4 my-5">
              <Col sm={8}>
                <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                  <Form.Control key={1} as="textarea" size="lg" type="text" placeholder={adventureLines} readOnly disabled rows={10} />
                </Form.Group>
              </Col>
              <Col >
                <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                  <Form.Control key={1} as="textarea" size="lg" type="text" placeholder={playerLines} readOnly disabled rows={10} />
                </Form.Group>
              </Col>
            </Row>
          </Row>

        </Container>
      </main>
    </div>
  )
}