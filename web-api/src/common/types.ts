interface Cycle {
  date: string;
  on: number[];
  off: number[];
}

interface LightPlan {
  name: string;
  value: Cycle[];
}
