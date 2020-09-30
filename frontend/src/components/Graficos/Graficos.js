import { data } from 'jquery';
import React,{Component} from 'react';
import Line from './Line/LineGraph'

class Graficos extends Component{
    intervalID;
    state = {
        url : ['http://18.221.219.89','http://18.223.23.220'],
        values : [0,0,0,0,0,0,0]
        
    }

    constructor(){
        super()
        this.getData = this.getData.bind(this)
        
    }

    componentDidMount(){
        document.title = "Graficos"
        this.getData()
        this.intervalID = setInterval(this.getData,5000)
    }

    componentWillUnmount() {
        clearTimeout(this.intervalID);
        console.log("Dejando de escuchar")
    }


    getData(){
        /*
        Promise.all([
            fetch(this.state.url[0]),
            fetch(this.state.url[1])
        ])
        .then(([res1, res2]) => Promise.all([res1.json(), res2.json()]))
        .then(([data1, data2]) => {
            //console.log(data1)
            //console.log(data2)
            this.values = [2,3]
        });
        */
       let newValue = this.state.values;
       newValue.push(Math.round(Math.random()*10))
       newValue.shift()
       this.setState({values : newValue})
    }

    

    render(){
        return(
            <main role="main" className="flex-shrink-0 mt-5 ">
                <div className="container-full py-md-5">
                    <div className="row ">
                        <div className="col-5">
                            <Line values={this.state.values} title = 'CPU 1' />
                        </div>
                        <div className="col-1"></div>
                        <div className="col-5">
                            <Line values={this.state.values} title = 'CPU 2' />
                        </div>
                    </div>
                    <div className="row ">
                        <div className="col-5">
                            <Line values={this.state.values} title = 'Memoria 1' />
                        </div>
                        <div className="col-1"></div>
                        <div className="col-5">
                            <Line values={this.state.values} title = 'Memoria 2' />
                        </div>
                    </div>
                    
                </div>
            </main>
        );
    }
}


export default Graficos