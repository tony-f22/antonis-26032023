import './App.css';
import Header from "./components/Header";
import Footer from "./components/Footer";
import {Container} from "react-bootstrap";
import HomeScreen from "./screens/HomeScreen";
import {HashRouter as Router, Route, Routes} from "react-router-dom";

function App() {
    return (
        <Router>
            <Header/>
            <main className="py-3">
                <Container>
                    <Routes>
                        <Route path='/' element={<HomeScreen/>}/>
                    </Routes>

                </Container>
            </main>
            <Footer/>
        </Router>
    );
}

export default App;
