"""
Here is a new kata that Codewars asked me to do related to interviewing and working in a production setting.

You might be familar with and have used Angular.js. Among other things, it lets you create your own filters that work as functions. You can then put these in a page to perform specific data changes, such as shortening a number to display a more concise notation.

In this kata, we will create a function which returns another function (or process, in Ruby) that shortens very long numbers. Given an initial array of values replace the Xth power of a given base. If the input of the returned function is not a numerical string, it should return the input itself as a string.

Here's an example, which is worth a thousand words:

filter1 = shorten_number(['','k','m'],1000)
filter1('234324') == '234k'
filter1('98234324') == '98m'
filter1([1,2,3]) == '[1,2,3]'
filter2 = shorten_number(['B','KB','MB','GB'],1024)
filter2('32') == '32B'
filter2('2100') == '2KB';
filter2('pippi') == 'pippi'

"""
def shorten_number(suffixes, base):
    
    def main(object):
        if type(object) == str and object.isdigit():
            result = None
            for i, suf in enumerate(suffixes):
                if i == 0:
                    divide_num = 1
                else:
                    divide_num = base**i
                divided = int(object) // divide_num
                if divided >= 1:
                    result = (str(divided) + suf)
                else:
                    break
            return result
        elif type(object) != str:
            return str(object)
        else:
            return object
        
    return main