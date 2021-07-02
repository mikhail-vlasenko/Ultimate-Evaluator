# The Ultimate Evaluator
Do you take notes in your favorite text editor and have to copy math to a calculator every time you want to get the result?

Here is the solution: a multifunctional calculator inside any text editor.

### Literally anywhere

Write text in any text field, press a hotkey, like ctrl + e, and you have a result typed right there

### Functionality

Evaluate anything from basic arithmetics, to full capabilities of WolframAlpha. 
Customization allows to fine-tune the Ultimate Evaluator for your purpose.

### Examples

`(0.5+0.8-0.2)*2` completes with ` = 2.2`

`log2(4*4)!` completes with ` = 24`

and even 
`\int[0,1] x^2 dx` gives ` -> integral_0^1 x^2 dx = 1/3 approx. 0.33333`

## Guide
### Installation
1. Download executable for windows or mac
2. Run the file
3. It will probably ask a few permissions, which are necessary to simulate key presses and access clipboard

### Usage
1. Put the cursor on the same line as the equation (or highlight the equation, depending on the input mode)
2. Press the hotkey (default `ctrl+e`)

The program will emulate `ctrl+c` (`cmd+c`) hotkey and will evaluate whatever appeared there.
Keep in mind that the current version does not restore previous clipboard value.

I, Mikhail Vlasenko, hereby promise (and you can easily see it in the source code) that 
user data and clipboard data is not sent anywhere.
