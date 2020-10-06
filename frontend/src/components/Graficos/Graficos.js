import { data } from 'jquery';
import React,{Component} from 'react';
import Line from './Line/LineGraph'

class Graficos extends Component{
    intervalID;
    state = {
        url : ['http://18.220.165.254:4200/','http://18.222.62.135:4200/'],
        cpu1 : [0,0,0,0,0,0,0],
        ram1 : [0,0,0,0,0,0,0],
        cpu2 : [0,0,0,0,0,0,0],
        ram2 : [0,0,0,0,0,0,0]

        
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
        
        Promise.all([
            fetch(this.state.url[0]),
            fetch(this.state.url[1])
        ])
        .then(([res1, res2]) => Promise.all([res1.json(), res2.json()]))
        .then(([data1, data2]) => {
            console.log(data1)
            console.log(data2)

            //------------ CPU 1
            let cp1 = data1['cpu']
            let newValue = this.state.cpu1
            newValue.push(+cp1)
            newValue.shift()
            this.setState({cpu1 : newValue})

            // ------------------ CPU 2
            let cp2 = data2['cpu']
            newValue = this.state.cpu2
            newValue.push(+cp2)
            newValue.shift()
            this.setState({cpu2 : newValue})

            //---------------- RAM 1 ------------
            let rm1 = data1['ram']
            newValue = this.state.ram1
            newValue.push(+rm1)
            newValue.shift()
            this.setState({ram1:newValue})

            //------------- RAM 2 ------------------
            let rm2 = data2['ram']
            newValue = this.state.ram2
            newValue.push(+rm2)
            newValue.shift()
            this.setState({ram2:newValue})

        });
        
       
        
       
    }

    

    render(){
        return(
            <main role="main" className="flex-shrink-0 mt-5 ">
                <div className="container-full py-md-5">
                    <div className="row ">
                        <div className="col-5">
                            <Line values={this.state.cpu1} title = 'CPU 1' />
                        </div>
                        <div className="col-1"></div>
                        <div className="col-5">
                            <Line values={this.state.cpu2} title = 'CPU 2' />
                        </div>
                    </div>
                    <div className="row ">
                        <div className="col-5">
                            <Line values={this.state.ram1} title = 'Memoria 1' />
                        </div>
                        <div className="col-1"></div>
                        <div className="col-5">
                            <Line values={this.state.ram2} title = 'Memoria 2' />
                        </div>
                    </div>
                    
                </div>
            </main>
        );
    }
}


export default Graficos