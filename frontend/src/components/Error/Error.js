import React,{Component} from 'react';

class Home extends Component{
    componentDidMount(){
        document.title = "Error 404"
    }

    render(){
        return(
            <div className="page">
                <p>Página no encontrada</p>
            </div>
        );
    }
}


export default Home;