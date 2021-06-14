class Tool {
    constructor(name, quantity, reservations) {
        this.name = name;
        this.quantity = quantity;
        this.reservations = reservations;

        render() {
            return `Tool: ${this.name}\nQuantity: ${this.quantity}`;
        }

    }
}

class ToolLibrary {
    constructor(tools) {
        this.tools = tools;
    }

    listTools(arr) {
        let tool_string = "Tool List:";
        arr.forEach(element => {
            let vals = (Object.values(element));
            let vals_string = `\nTool: ${vals[0]}\nQuantity: ${vals[1]}\nReserve Now!
        Donate Tool!\n---`
            tool_string += vals_string;
        });
        return tool_string;

    }
}

const hammer = new Tool('Hammer', 35, []);
const axe = new Tool('Axe', 18, []);
const tools = [hammer, axe];

const toolLibrary = new ToolLibrary(tools);
