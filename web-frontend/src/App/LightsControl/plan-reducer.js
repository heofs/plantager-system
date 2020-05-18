export const initialState = [{ date: 'start', on: [6, 0], off: [21, 0] }];

export const reducer = (state, action) => {
  let newState = [];

  switch (action.type) {
    case 'setPlan':
      return action.payload;

    case 'setStartCycle':
      newState = [...state];
      newState[0].on = [action.payload[0], 0];
      newState[0].off = [action.payload[1], 0];
      return newState;

    case 'setDateCycle':
      newState = [...state];
      newState[action.payload.index].on = [action.payload.range[0], 0];
      newState[action.payload.index].off = [action.payload.range[1], 0];
      return newState;

    default:
      return state;
  }
};
