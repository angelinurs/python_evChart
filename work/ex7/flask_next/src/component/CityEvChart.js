import React from 'react';

import { useState, useEffect } from 'react';
import Axios from "axios";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Ev Stations Bar Chart',
    },
  },
};

export function CityEvChart() {
    const [ list, setList ] = useState([]);

    function getData() {
        Axios.get(
            'http://127.0.0.1:5000/evChart',

            // {
            //   headers: {
            //     'Content-type' : 'application/json',
            //     'Access-Control-allow-Origin' : '*'
            //   },
            // },

        ).then( (res) => {
            console.log( res.data );
            setList( list );

        });
    };

    useEffect(()=>{
        getData();
    }, []);
    
    const data = {
        labels: list.map( x=> x.local ),
        datasets: [
            {
            label: '전국 전기차 충전소 현황',
            data: list.map( x => x.count ),
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            },
        ],
    };

    return <Bar options={options} data={data} />;
}
