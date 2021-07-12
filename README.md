# The Ultimate Evaluator
Do you take notes in your favorite text editor and have to copy math to a calculator every time you want to get the result?

Here is the solution: a multifunctional **calculator inside any text editor**.

### Literally anywhere

Write text in any text field, press a hotkey, like `ctrl+e`, and you have a result typed right there!

### Functionality

Evaluate anything from basic arithmetics, to full capabilities of WolframAlpha. 
Customization allows to fine-tune the Ultimate Evaluator for your purpose.

#### Eval modes overview
**Basic** is suitable for arithmetics (including simple factorials `7!`, but not `(5+2)!`). 
Works fine even if some unrelated text is found in the clipboard.

**Advanced** is suitable for most computations one does: evaluates logarithms, trigonometry, etc.

**Wofram** uses WoframAlpha's API for computation, which makes it by far the most powerful method. 
Takes more time than other methods and requires internet connection. 
You need to insert appid to get it working. (look instructions below)

### Examples

`(0.5+0.8-0.2)*2` completes with ` = 2.2`

`log2(4*4)!` completes with ` = 24`

and even `\int[0,1] x^2 dx` gives ` -> integral_0^1 x^2 dx = 1/3 approx. 0.33333`

### Demonstration in Notion text editor

https://user-images.githubusercontent.com/27450370/124346445-23381500-dbdf-11eb-9513-98fe400f5324.mov

https://user-images.githubusercontent.com/27450370/124346451-2a5f2300-dbdf-11eb-93f2-041b83710a76.mov

https://user-images.githubusercontent.com/27450370/124346472-4ebaff80-dbdf-11eb-8fbf-74860b49fbd1.mov

## Guide
### Installation
1. Download executable for [windows](https://drive.google.com/file/d/1ieW2f2geV105gMsCel46d804DeuvExuR/view?usp=sharing) or [mac](https://drive.google.com/file/d/1YkgpJ6i_KIPKel3oz_A6i75Ke7bJ8sXT/view?usp=sharing)
2. Unzip the file (for mac also move the app to the Applications folder)
3. Run the executable. Since I am an unidentified developer, MacOS will only let you run the file if you right-click it, then select *open* in drop-down menu, and finally click *Open* in the appeared window. 
4. It will probably ask a few permissions, which are necessary to simulate key presses and access clipboard
5. Default hotkeys may not work, but you can always reassign them. (see instructions below)

### Usage
1. Put the cursor on the same line as the equation (or highlight the equation, depending on a hotkey you are going to press)
2. Press the hotkey (default or the one you have set)
3. No third step, it's as simple as that!

The app will start evaluating only after all shortcut keys are released. It is important not to hold any keys in the next moment.

The program will emulate `ctrl+c` (`cmd+c`) hotkey and will evaluate whatever appeared there.
Keep in mind that the current version does not restore previous clipboard value.

### How to assign hotkeys
Click one of the 'set hotkey' buttons. In the next 3 seconds you have to press the desired hotkey (no more than 3 keys).

Make sure the hotkey does not conflict with other functions. Recommended for windows: `ctrl+alt+e`, `ctrl+alt+h`; for mac: `f10`

### Do I need the *highlight* hotkey or the *main* one?
To decide this, open the editor and write something. Press `ctrl(cmd)+c` and look what happens. 
1. Nothing seems to happen but your clipboard is updated with the whole line -> just press the main combination to evaluate (`ctrl+alt+e`). Examples: Notion, Sublime 3.
2. Nothing happens and the clipboard is not updated -> you will have to highlight the equation and press highlight shortcut (`ctrl+alt+h`) to evaluate. Examples: Google Docs
3. The whole line is highlighted and the clipboard is updated -> highlight shortcut (`ctrl+alt+h`)

### How to use Wolfram mode
To use it, you need to provide the application with the [wolfram API](https://products.wolframalpha.com/api/) appid. 
You can get 2000 requests per month for free. 
Appid has format XXXXXX-XXXXXXXXXX 

## [Troubleshooting](https://github.com/mikhail-vlasenko/Ultimate-Evaluator/blob/master/docs/troubleshooting.md#troubleshooting)

### Warnings
The application, especially the advanced evaluation mode, is still under testing and may occasionally produce incorrect results.
It relies on the user to provide it with valid inputs.

Basic eval mode ignore all letters in the input string and thus (currently) merges all equations into one, 
which can lead to unexpected behaviour.

### No personal data is shared
I, Mikhail Vlasenko, hereby promise (and you can easily see it in the source code) that 
user data and clipboard data is not sent anywhere.

### Feedback
All feedback is highly appreciated. Except criticism of GUI appearance.

You can reach me via email, issues on github, or Telegram, if you know it
