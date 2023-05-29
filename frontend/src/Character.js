import React, { useState, useEffect } from "react"
import { Image, Nav, Navbar, Container, Row, Col, Form, Button } from 'react-bootstrap'

function InfoField(props) {
  return <div>
    <Form.Label>{props.label}</Form.Label>
    <Form.Control as="textarea" size="lg" type="text" placeholder={props.content} readOnly disabled rows={props.rows}/>
    <br />
  </div>
}

export const Character = () => {
  const [characterInfo, setCharacterInfo] = useState({})

  useEffect(() => {
    fetch("/getCharacter").then(
      res => res.json()
    ).then(
      data => {
        console.log(data)
        console.log(JSON.parse(data.characterInfo))
        setCharacterInfo(JSON.parse(data.characterInfo))
      }
    )
  }, [])
  return <div className='App'>
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
          <Col sm={4}>
            <Image width="80%" height="80%" fluid rounded thumbnail src={characterInfo.currentImage} className="" />
            <Button> Play an adventure</Button>
          </Col>
          <Col>
            <InfoField label="Name" content={characterInfo.name}/>
            <InfoField label="Level" content={characterInfo.level}/>
            <InfoField label="Number Of Adventures" content={characterInfo.numberOfAdventures}/>
            <InfoField label="Description" content={characterInfo.description} rows={8}/>
            <InfoField label="Main Weapon" content={characterInfo.mainWeapon}/>
            <InfoField label="Journal" content={characterInfo.journal} rows={8}/>
          </Col>
        </Row>
      </Container>
    </main>
  </div>
}