import { NavLink } from "react-router-dom";


const Header = () => {
    return (
        <div>
            <nav>
                <ul className='header'>
                    <li><NavLink to='/'>Review Graph</NavLink></li>
                    <li><NavLink to='/movie'>Movie Recommendations</NavLink></li>
                    <li><NavLink to='/recommendations'>Recommendations</NavLink></li>
                    <li><NavLink to='/neighbors'>Neighbors</NavLink></li>
                    <li><NavLink to='/evaluation'>Evaluation</NavLink></li>
                    <li><NavLink to='/sentiment'>Sentiment</NavLink></li>
                </ul>
            </nav>
        </div >
    )
}

export default Header;