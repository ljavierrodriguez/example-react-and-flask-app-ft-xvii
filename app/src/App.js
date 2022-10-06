import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Agendas from './views/Agendas';
import Home from './views/Home';

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/users/:id/agendas" element={<Agendas />} />
                <Route path="/" element={<Home />} />
            </Routes>
        </BrowserRouter>
    )

}

export default App;