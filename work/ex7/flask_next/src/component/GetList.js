import Axios from "axios";
import { useState, useEffect } from "react";

function GetList() {
    const [list, setList] = useState([]);

    function getData() {
        Axios.get(
            'http://127.0.0.1:5000/evChart'
        ).then( (res) => {
            console.log( res.data );
        });
    }

    useEffect( () =>{
        getData();
    }, [] );

    return (
        <div className="getList">

        </div>
    );
}

export default GetList;