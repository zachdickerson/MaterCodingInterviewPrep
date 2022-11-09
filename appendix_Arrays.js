/* -------   Creating a array class   --------- */

/* Arrays in JavaScript are just objects with integer based keys that
   Act like indexes.
*/

/* Our Class */
class MyArray {
    constructor() {
        /* 2 - data points */
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
        const lastItem = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--;
        return item;
    }

    delete(index) {
        const item = this.data[index];
        this.shiftItems(index);
        return lastItem;
    }

    shiftItems() {
        for (let i = index; i < this.length-1; i++) {
            this.data[i] = this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length--;
    }
}

const newArray = new MyArray();
newArray.push('hi');
newArray.push('you');
newArray.push('!');
newArray.pop();
console.log(newArray);