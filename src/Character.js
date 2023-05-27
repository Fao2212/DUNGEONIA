import React, {useState,useEffect} from "react"
import {Image,Nav,Navbar,Container} from 'react-bootstrap'
export const Character = () =>
{
    const [characterInfo,setCharacterInfo] = useState({})

    useEffect(()=>{
      fetch("/getCharacter").then(
        res => res.json()
      ).then(
        data =>{
            setCharacterInfo(data)
            console.log(data)
            console.log(data.characterInfo)
        }
      )
    },[])
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
        <Image fluid rounded src={characterInfo.currentImage} className=""/>
      </Container>
    </main>
  </div>
}