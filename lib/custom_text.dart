import 'package:flutter/material.dart';

class CustomText extends StatelessWidget{
  const CustomText({super.key});
  
  @override
  Widget build(BuildContext context){
    return Text("Hello World",
                  style: TextStyle(
                    color: Color.fromARGB(255, 0, 0, 0),
                    fontSize: 70,
                  ));
  }
}