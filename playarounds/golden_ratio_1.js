// Created in p5.js web editor

const N = 17;
let COLORS = [];
let count;

function setup() {
  let dim = Math.pow(2, 10);
  createCanvas(dim, dim);
  rectMode(CENTER);
  randomSeed(42);
  for (let i = 0; i <= N; ++i) {
    COLORS.push(
      color(
        random(0, 256),
        random(0, 256),
        random(0, 256)
      )
    );
  }
}

function draw() {
  background(220);
  // makeColors();
  goldenRectangle(683, 341, 2);
}

function makeColors() {
  COLORS = [];
  randomSeed(parseInt(mouseX));
  for (let i = 0; i <= N; ++i) {
    COLORS.push(
      color(
        random(0, 256),
        random(0, 256),
        random(0, 256)
      )
    );
  }
}

function goldenRectangle(x, y, initialSize) {
  square(x, y, initialSize);
  let shape = 'rect';
  let direction = createVector(1, 0);
  let w = initialSize;
  let centre = createVector(x, y);

  count = 0;

  nextShape(centre, w, shape, direction);
}

function nextShape(previousCentre, previousWidth, previousShape, previousDirection) {
  let shape = previousShape === 'square' ? 'rect' : 'square';
  let direction = previousDirection.rotate(HALF_PI);

  let translation = direction.copy();
  let p = previousCentre.copy();
  translation.mult(previousWidth);
  let thisCentre = p.add(translation);
  let centre = createVector(
    (previousCentre.x + thisCentre.x) / 2,
    (previousCentre.y + thisCentre.y) / 2
  );

  let w = previousWidth,
      h = previousWidth;

  if (shape === 'rect') {
    h = h * 2;
    if (Math.floor(direction.x) === 0) {
      let t = w;
      h = w;
      w = t;
    }
  }

  fill(COLORS[count]);
  rect(thisCentre.x, thisCentre.y, w, h);

  if (count < N ) {
    count = count + 1;
    nextShape(centre, h, shape, direction);
  }
}
