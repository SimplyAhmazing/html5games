$(document).ready(function(){
	var canvas  = $("#canvas")[0];
	var ctx = canvas.getContext("2d");
	var w = $("#canvas").width();
	var h = $("#canvas").height();

	//width of a snake cell
	var cw = 10;
	var d; //default direction
	var food;
	var score;

	//lets create the snake
	var snake_array; //an array of empty cells to make up the snake

	function init(){

		
		d = "right";

		create_snake();
		create_food();
		score = 0;

		//move the snake using a timer that will trigger the paint ftn
		//every 60ms
		if(typeof game_loop != "undefined") clearInterval(game_loop);
		game_loop = setInterval(paint, 60);
	}

	init();

	function create_snake(){
		var length = 5;
		snake_array = [];
		for(var i = length-1; i >= 0; i--){
			//this will create
			snake_array.push({x:i,y:0});
		}
	}


	function create_food(){
		food = {
			x: Math.round(Math.random()*(w-cw)/cw),
			y: Math.round(Math.random()*(w-cw)/cw),
		};
	}
	

	//lets pain the snake now
	function paint(){
		//clear out canvas
		//lets paint the canvas now
		ctx.fillStyle = "white";
		ctx.fillRect(0,0,w,h);
		ctx.strokeStyle = "black";
		ctx.strokeRect(0,0,w,h);

		//movement code for the snake
		var nx = snake_array[0].x;
		var ny = snake_array[0].y;

		//increment head to get new position
		if (d=="right") nx++;
		else if (d=="left") nx--;
		else if (d=="down") ny++;
		else if (d=="up") ny--;

		//restart the game if the snake hits the wall
		if(nx == -1 || nx == w/cw || ny == -1 || ny == h/cw || collision_check(nx, ny, snake_array)){
			//restart the game
			init();
			return; //breaks the paint function...
		}

		if( nx == food.x && ny == food.y){
			var tail = {x: nx, y: ny};
			//create food
			create_food();
		}else{
			var tail = snake_array.pop(); //pops out the last cell
			tail.x = nx; tail.y = ny;
		}


		snake_array.unshift(tail); //puts back the tail as the first cell


		for(var i=0; i < snake_array.length; i++){
			var c = snake_array[i];
			//lets paint 10px
			paint_cell(c.x, c.y);
		}

		//paint food
		paint_cell(food.x, food.y);
	}


	function collision_check(x,y, sn_array){
		for(var i = 0; i < sn_array.length; i++){
			
			if (x == sn_array[i].x && y == sn_array[i].y){
				return true;
			}
			
			return false;
			
		}
	}


	//generic ftn to draw cells
	function paint_cell(x,y){
		//lets paint 10px
		ctx.fillStyle = "blue";
		ctx.fillRect(x*cw, y*cw,cw,cw);
		ctx.strokeStyle = "white";
		ctx.strokeRect(x*cw, y*cw, cw, cw);
	}

	//keyboard controls
	$(document).keydown(function(e){
		var key = e.which;
		if (key == "37" && d != "right") d = "left";
		else if (key == "38" && d != "down") d = "up";
		else if (key == "39" && d != "left") d = "right";
		else if (key == "40" && d != "up") d = "down";

	});

	
})
