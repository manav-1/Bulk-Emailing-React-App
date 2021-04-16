import "../CSS/style.css";
import React, { Component } from "react";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  ScrollView,
  ActivityIndicator,
  TouchableOpacity,
} from "react-native";
import BasicButton from "./BasicButton";
import LoginSignUp from "./LoginSignUpBtn";
import ValidationComponent from "react-native-form-validator";
import SnackBar from "./Snackbar";
import Ionicons from "react-native-vector-icons/Ionicons";
import axios from "axios";

export default class SignUp extends ValidationComponent {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
      sno: "",
      eno: "",
      link: "",
      subject: "",
      snackBarVisible: false,
      snackBarType: "",
      snackBarText: "",
      hidden: true,
      file: null,
    };
  }
  onFileChange = (event) => {
    this.setState({ file: event.target.files[0] });
    console.log(this.state.file);
  };

  displaySnackBar = (type, text) => {
    this.setState({
      snackBarType: type,
      snackBarText: text,
      snackBarVisible: true,
    });
  };

  hideSnackBar = () => {
    this.setState({
      snackBarVisible: false,
    });
  };
  //function to handle when signup btn is clicked on
  handleRegisterBtnClick = () => {
    console.log("inside register button click");
    this.validate({
      email: { email: true, required: true },
      password: { required: true },
      sno: { required: true },
      eno: { required: true },
      link: { required: true },
      subject: { required: true },
    });
    if (this.getErrorMessages()) {
      this.displaySnackBar("error", this.getErrorMessages());
    } else {
      this.displaySnackBar("success", "Sent to API Successfully");
      //sending the data
      let formdata = new FormData();
      formdata.append("file", this.state.file, this.state.file.name);
      formdata.append("email", this.state.email);
      formdata.append("password", this.state.password);
      formdata.append("sno", this.state.sno);
      formdata.append("eno", this.state.eno);
      formdata.append("link", this.state.link);
      formdata.append("subject", this.state.subject);
      // var data = {
      //   email: this.state.email,
      //   password: this.state.password,
      //   sno: this.state.sno,
      //   eno: this.state.eno,
      //   link: this.state.link,
      //   subject: this.state.subject,
      //   file: this.state.file
      // };
      axios.post("http://127.0.0.1:5000/api", formdata).then((res) => {
        console.log("inside then");
        console.log(res);
        if (res.data === "Done") {
          this.displaySnackBar("success", "Mails are sent successfully");
        } else if (res.data === "cred") {
          this.displaySnackBar("error", "Check your email and password once");
        } else if (res.data === "link") {
          this.displaySnackBar("error", "Check your sheet link once");
        } else if (res.data === "error") {
          this.displaySnackBar(
            "error",
            "There is some error, please Try again later"
          );
        }
      });
    }
    // axios.get(`http:127.0.0.1:5000/api?email=${this.state.email}&password=${this.state.password}&sno=${this.state.sno}&eno=${this.state.eno}&link=${this.state.link}&subject=${this.state.subject}`).then((res)=>{
    //   console.log("inside then")
    //   console.log(res)
    // })
    // }
  };
  hideShow = () => {
    this.setState({ hidden: !this.state.hidden });
  };

  //component rendering
  render() {
    var icon = this.state.hidden ? "eye-outline" : "eye-off-outline";
    return (
      <>
        <ScrollView style={styles.container}>
          <Text style={styles.title}>Email Server</Text>

          <View style={styles.form}>
            <View style={styles.divider}></View>
            <Text style={styles.label}>Email Address</Text>
            <TextInput
              style={styles.inputField}
              keyboardType="email-address"
              placeholder="Enter your registered email"
              value={this.state.email}
              onChangeText={(email) => this.setState({ email })}
            />

            <View style={styles.divider}></View>
            <Text style={styles.label}>Password</Text>
            <View style={styles.password}>
              <TextInput
                style={styles.inputFieldp}
                secureTextEntry={this.state.hidden}
                placeholder="Enter password"
                value={this.state.password}
                onChangeText={(password) => this.setState({ password })}
              />
              <TouchableOpacity onPress={this.hideShow}>
                <Ionicons name={icon} style={{ fontSize: 25 }} />
              </TouchableOpacity>
            </View>

            <View style={styles.divider}></View>
            <Text style={styles.label}>Enter the Sheet Link</Text>
            <TextInput
              style={styles.inputField}
              placeholder="Enter your Sheet Link"
              value={this.state.link}
              onChangeText={(link) => this.setState({ link })}
            />
            <View style={styles.divider}></View>
            <Text style={styles.label}>Subject</Text>
            <TextInput
              style={styles.inputField}
              placeholder="Enter the Subject"
              value={this.state.subject}
              onChangeText={(subject) => this.setState({ subject })}
            />
            <View style={styles.divider}></View>
            <Text style={styles.label}>Starting Number</Text>
            <TextInput
              style={styles.inputField}
              placeholder="Enter the starting number"
              value={this.state.sno}
              onChangeText={(sno) => this.setState({ sno })}
            />
            <View style={styles.divider}></View>
            <Text style={styles.label}>Ending Number</Text>
            <TextInput
              style={styles.inputField}
              placeholder="Enter the ending number"
              value={this.state.eno}
              onChangeText={(eno) => this.setState({ eno })}
            />
          </View>
          <label className="fileLabel">
            <input
              className="fileInput"
              size="1000"
              type="file"
              onChange={this.onFileChange}
            />
            Upload Files
          </label>
          <View style={styles.divider}></View>

          <BasicButton
            text="Send Emails"
            onPress={this.handleRegisterBtnClick}
          />
        </ScrollView>
        {this.state.snackBarVisible ? (
          <SnackBar
            isVisible={this.state.snackBarVisible}
            text={this.state.snackBarText}
            type={this.state.snackBarType}
            onClose={this.hideSnackBar}
          />
        ) : null}
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    paddingVertical: 30,
    flex: 1,
    backgroundColor: "#fff",
    paddingHorizontal: 30,
  },

  title: {
    fontWeight: "700",
    fontSize: 30,
    letterSpacing: 0.1,
    color: "#2E2E2E",
  },

  form: {
    marginVertical: 10,
  },

  label: {
    fontSize: 16,
    lineHeight: 18,
    color: "#666666",
    marginBottom: 3,
  },

  inputField: {
    fontSize: 14,
    borderWidth: 0,
    borderBottomWidth: 1,
    borderBottomColor: "#BFBFBF",
    paddingVertical: 6,
  },

  divider: {
    paddingVertical: 8,
  },

  log: {
    textAlign: "center",
    marginVertical: 2,
    color: "red",
  },

  signin: {
    marginVertical: 40,
  },
  password: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-between",
  },
  inputFieldp: {
    fontSize: 14,
    borderWidth: 0,
    borderBottomWidth: 1,
    borderBottomColor: "#BFBFBF",
    paddingVertical: 6,
    width: "100%",
  },
});
