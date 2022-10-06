import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    const [users, setUsers] = useState(null);

    useEffect(() => {

        fetchUsers(`${process.env.REACT_APP_API_URL}/api/users`)

    }, [])

    const fetchUsers = async (url) => {
        try {

            const response = await fetch(url);
            const data = await response.json()

            setUsers(data);

        } catch (error) {
            console.log(error)
        }
    }

    const addAgenda = async (url, id) => {
        try {

            const info = {
                title: 'Prueba New Agenda',
                users_id: id
            }

            const response = await fetch(url, {
               method: 'POST',
               headers: {
                'Content-Type': 'application/json'
               },
               body: JSON.stringify(info)
            });
            const data = await response.json()

            console.log(data);

        } catch (error) {
            console.log(error)
        }
    }

    return (
        <>
            <h1>Home</h1>
            {/* <ul className="list-group w-50 mx-auto">
                {
                    !!users &&
                    users.map((user) => {
                        return (
                            <li key={user.id} className="list-group-item">{user.username}</li>
                        )
                    })
                }
            </ul> */}
            <ol className="list-group list-group-numbered w-50 mx-auto">
                {
                    !!users &&
                    users.map((user) => {
                        return (
                            <li className="list-group-item d-flex justify-content-between align-items-start" key={user.id}>
                                <div className="ms-2 me-auto">
                                    <div className="fw-bold">{user.username}</div>
                                </div>
                                <Link className="badge bg-primary rounded-pill" to={"/users/"+user.id+"/agendas"}>Ver Agendas</Link>
                                <button className="badge bg-primary rounded-pill" onClick={() => addAgenda(`${process.env.REACT_APP_API_URL}/api/agendas`, user.id)}>Add Agenda</button>
                            </li>
                        )
                    })
                }


            </ol>
        </>
    )
}

export default Home;