import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

const Agendas = () => {
    const [agendas, setAgendas] = useState(null);
    const { id } = useParams();

    useEffect(() => {

        fetchAgendas(`${process.env.REACT_APP_API_URL}/api/users/${id}/agendas`)

    }, [])

    const fetchAgendas = async (url) => {
        try {

            const response = await fetch(url);
            const data = await response.json()
            console.log(data);
            const { agendas } = data;
            setAgendas(agendas);

        } catch (error) {
            console.log(error)
        }
    }

    return (
        <>
            <h1>Agendas</h1>
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
                    !!agendas &&
                    agendas.map((agenda) => {
                        return (
                            <li className="list-group-item d-flex justify-content-between align-items-start" key={agenda.id}>
                                <div className="ms-2 me-auto">
                                    <div className="fw-bold">{agenda.title}</div>
                                    {agenda.owner}
                                </div>
                                <Link className="badge bg-primary rounded-pill" to={"/users/"+agenda.users_id+"/agendas/contacts"}>Ver Contacts</Link>
                            </li>
                        )
                    })
                }


            </ol>
        </>
    )
}

export default Agendas;