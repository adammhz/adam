import 'package:flutter/material.dart';

class CustomButton extends StatelessWidget{
  const CustomButton({super.key});
  
  @override
  Widget build(BuildContext context){
    return TextButton(
      onPressed: (){},
      child: Text("Click Me!", style: TextStyle(color: Colors.black)),
    );
  }
}