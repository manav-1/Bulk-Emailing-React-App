import React from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default function LoginSignUpBtn({
  customStyle,
  text,
  btnText,
  onPress,
}) {
  return (
    <View style={[styles.container, customStyle]}>
      <Text style={styles.text}>{text}</Text>
      <TouchableOpacity onPress={onPress}>
        <Text style={styles.btnText}>{btnText}</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    fontSize: 16,
    lineHeight: 20,
    flexDirection: "row",
    alignItems: "center",
  },

  text: {
    fontSize: 16,
    lineHeight: 20,
  },

  btnText: {
    fontWeight: "500",
    fontSize: 17,
    lineHeight: 20,
    color: "#2B35E0",
    marginLeft: 2,
  },
});
