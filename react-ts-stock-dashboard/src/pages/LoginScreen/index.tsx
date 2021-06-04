import React from 'react';
import logo from '../../assets/kite-logo.svg';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import '../../styles/login-screen-styles.css';
import { makeStyles, createStyles, Theme } from '@material-ui/core/styles';
import Link from '@material-ui/core/Link';
// import Typography from '@material-ui/core/Typography';


const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            background: "black"
        },
        input: {
            color: "white"
        }
    }),
);

function LoginScreen() {

    const classes = useStyles();
    const preventDefault = (event: React.SyntheticEvent) => event.preventDefault();

    return (
        <div className="login-screen">
            <div className="login-header">
                <div className="Logo">
                    <img src={logo} className="dashboard-logo" alt="dashboard-logo" />
                </div>
                <div className="login-title">
                    Login to Stock Dashboard
                </div>
                <div className="login-form">
                    <form autoComplete="off">
                        <div className="login-user-id-textfield">
                            <TextField
                                required
                                id="outlined-required"
                                label="User ID"
                                className={classes.root}
                                // defaultValue="Hello World"
                                variant="outlined"
                                fullWidth
                                InputProps={{
                                    className: classes.input
                                }}
                                InputLabelProps={{
                                    style: {
                                        textOverflow: 'ellipsis',
                                        whiteSpace: 'nowrap',
                                        overflow: 'hidden',
                                        width: '100%',
                                        color: 'grey'
                                    }
                                }}
                            />
                        </div>
                        <div className="login-password-textfield">
                            <TextField
                                required
                                id="outlined-password-input"
                                label="Password"
                                type="password"
                                autoComplete="current-password"
                                className={classes.root}
                                variant="outlined"
                                fullWidth
                                InputProps={{
                                    className: classes.input
                                }}
                                InputLabelProps={{
                                    style: {
                                        textOverflow: 'ellipsis',
                                        whiteSpace: 'nowrap',
                                        overflow: 'hidden',
                                        width: '100%',
                                        color: 'grey'
                                    }
                                }}
                            />
                        </div>
                        <Button variant="contained" className="login-btn-container">
                            <p className="login-btn-text">Login</p>
                        </Button>
                    </form>
                </div>
            </div >
            <div className="login-footer">
                <Link href="/register" onClick={preventDefault}>
                    Don't have an account? Signup now!
                </Link>
            </div>
        </div >
    );
}

export default LoginScreen;