import React from 'react';
import { useEffect, useState } from "react";


const AgenciPage = () => {
  const [agents, setAgents] = useState([]);
  const [agent, setAgent] = useState({imie: '', nazwisko: '', nr_licencji: ''});

useEffect(() => {
  const fetchAgents = async ()=> {
    try{
    const agents_response = fetch('http://127.0.0.1:8080/agenci/')
    const data = await agents_response.json()
    setAgent(data)
    console.log(data)
    }catch (err) {
      console.error('Error fetching agents:', err);
    }
  }
  fetchAgents();
}, []);

  return (
      <h1>Agenci</h1>,
  <ul>
    {agents.map((agent) => (
        <li key={agent.id}>
          {agent.imie} {agent.nazwisko} {agent.nr_licencji}
        </li>
          ))}
  </ul>

  );
};

export default AgenciPage;
