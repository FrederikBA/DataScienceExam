import { NavLink } from "react-router-dom";


const Header = () => {
    return (
        <div>
            <nav>
                <ul className='header'>
                    <li><NavLink to='/'>Review Graph</NavLink></li>
                    <li><NavLink to='/earnings'>Predict Earnings</NavLink></li>
                    <li><NavLink to='/movie'>Movie Recommendations</NavLink></li>
                    <li><NavLink to='/sentiment'>Sentiment Prediction</NavLink></li>
                </ul>
            </nav>
        </div >
    )
}

export default Header;