# Introduction

cssreporter is small tools for detect how many properties and values you are typed.it's next css generation reporter who want to improve your css and avoid maximum repetition as much you can.

# how to run

```
from cssreporter import css_reporter

css_reporter('your css filename with extension')



Hello !! 

successfully created a complete report about your css file

file name - css_complete_report.txt

 ------thank you for using cssreporter :)----------------

```


# benefits

- reduce repetition
- avoid bloat css codes
- how many lines of code written
- complete code report specifically based by properties you are typed

# Most Highlights About cssreporter:

- you can clearly see how much time you were repeats same values and properties.


# how it's exactly output from your css file?

### css_complete_report.txt   =>
```
--------------------------------
    background-color - 6 lnofcode
    --------------------------------
    - hsla(0,0%,100%,.99); 
    - SelectedItem; 
    - hsl(0, 0%, 97%); 
    - SelectedItem; 
    - hsl(0, 0%, 90%); 
    - hsl(0, 0%, 85%); 

    --------------------------------
    color - 9 lnofcode
    --------------------------------
    - hsla(0,0%,100%,.99); 
    - black; 
    - SelectedItem; 
    - SelectedItemText; 
    - hsl(0, 0%, 97%); 
    - #666; 
    - SelectedItem; 
    - hsl(0, 0%, 90%); 
    - hsl(0, 0%, 85%); 

    --------------------------------
    border - 10 lnofcode
    --------------------------------
    - 1px solid hsla(0, 0%, 0%, .2); 
    - none; 
    - 1px solid hsl(0, 0%, 92%); 
    - 0; 
    - 1px solid hsl(0, 0%, 92%); 
    - 0; 
    - none; 
    - 1px solid hsl(0, 0%, 92%); 
    - none; 
    - 1px solid hsla(0, 0%, 0%, .08); 

    --------------------------------
    border-top - 2 lnofcode
    --------------------------------
    - none; 
    - 1px solid hsla(0, 0%, 0%, .08); 

    --------------------------------
    box-shadow - 1 lnofcode
    --------------------------------
    - 0 5px 10px hsla(0, 0%, 0%, .1); 

    --------------------------------
    position - 3 lnofcode
    --------------------------------
    - absolute; 
    - right center; 
    - left; 
```

# friendly output when it's successfully reports :)

 ```
Hello !! 

successfully created a complete report about your css file

file name - css_complete_report.txt

 ------thank you for using cssreporter :)------------------
 ```

 # Copyright & License

 Suresh P @ 2022 | cssreporter | Unlicense
