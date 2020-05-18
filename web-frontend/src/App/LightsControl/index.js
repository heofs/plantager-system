import React, { useState, useEffect } from 'react';
import { Slider, Button, Row, Col } from 'antd';
import { PlusCircleOutlined } from '@ant-design/icons';
import { useQuery, useMutation } from '@apollo/react-hooks';
import { GET_LIGHT_CYCLE, UPDATE_LIGHT_CYCLE } from 'graphql/light-cycle';
import ConfirmationModal from './confirmation-modal';

const marks = {};
for (let x = 0; x <= 24; x++) {
  marks[x] = `${x}h`;
}

export const LightsControl = () => {
  const default_lights = [0, 24];
  const [lightsRange, setLightsRange] = useState(default_lights);
  const [modalVisible, setModalVisible] = useState(false);
  const { loading, data } = useQuery(GET_LIGHT_CYCLE, {
    fetchPolicy: 'network-only',
  });
  const [updateLights] = useMutation(UPDATE_LIGHT_CYCLE);

  const handleSave = () => {
    setModalVisible(true);
  };

  useEffect(() => {
    if (!loading && data && data.lightCycle) {
      const startCycle = data.lightCycle.value[0];
      setLightsRange([startCycle.on[0], startCycle.off[0]]);
    }
  }, [loading, data]);

  return (
    <Row gutter={[8, 16]}>
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
          disabled={loading}
        />
      </Col>
      <Col span={24} flex="auto" style={{ textAlign: 'center' }}>
        <Button
          type="primary"
          shape="circle"
          icon={<PlusCircleOutlined />}
          size={'large'}
        />
      </Col>
      <Col span={24}>
        <Button type="primary" block onClick={handleSave}>
          Save
        </Button>
      </Col>
      <ConfirmationModal
        lightsRange={lightsRange}
        modalVisible={modalVisible}
        setModalVisible={setModalVisible}
        onConfirm={() =>
          updateLights({
            variables: {
              lightCycle: [
                {
                  date: 'start',
                  on: [lightsRange[0], 0],
                  off: [lightsRange[1], 0],
                },
              ],
            },
          })
        }
      />
    </Row>
  );
};

export default LightsControl;
