import React, { useState, useEffect } from 'react';
import { Slider, Button, Modal, Row, Col } from 'antd';
import { useQuery } from '@apollo/react-hooks';

import { GET_LIGHT_CYCLE } from 'graphql/light-cycle';

const marks = {};
for (let x = 0; x <= 24; x++) {
  marks[x] = `${x}h`;
}

export const LightsControl = () => {
  const default_lights = [0, 24];
  const [lightsRange, setLightsRange] = useState(default_lights);
  const [modalText, setModalText] = useState('Content of the modal');
  const [modalVisible, setModalVisible] = useState(false);
  const [confirmLoading, setConfirmLoading] = useState(false);
  const { loading, data } = useQuery(GET_LIGHT_CYCLE, {
    fetchPolicy: 'network-only',
  });

  const handleSave = () => {
    console.log(lightsRange);
    setModalText(
      `Lights will turn on at ${lightsRange[0]}:00 and off at ${lightsRange[1]}:00`
    );
    setModalVisible(true);
  };

  const handleOk = () => {
    setConfirmLoading(true);

    // FIRE MUTATION WITH lights then
    setModalVisible(false);
    setConfirmLoading(false);
  };

  const handleCancel = () => {
    console.log('Clicked cancel button');
    setModalVisible(false);
  };

  useEffect(() => {
    if (!loading && data && data.lightCycle) {
      const startCycle = data.lightCycle.value[0];
      setLightsRange([startCycle.on[0], startCycle.off[0]]);
    }
  }, [loading, data]);

  return (
    <Row>
      <Col span={24}>
        <h2 style={{ textAlign: 'center' }}>Set lights cycle</h2>
      </Col>
      <Col span={24}>
        <Slider
          range
          marks={marks}
          defaultValue={default_lights}
          max={24}
          dots={true}
          value={lightsRange}
          onChange={(range) => setLightsRange(range)}
        />
      </Col>
      <Col span={24}>
        <Button type="primary" block onClick={handleSave}>
          Save
        </Button>
      </Col>
      <Modal
        title="Change lights cycle"
        visible={modalVisible}
        onOk={handleOk}
        confirmLoading={confirmLoading}
        onCancel={handleCancel}
      >
        <p>{modalText}</p>
      </Modal>
    </Row>
  );
};

export default LightsControl;
